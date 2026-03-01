program DuplicateHunter;

{$mode objfpc}{$H+}

uses
  SysUtils, 
  Classes; 

type
  TFileData = record 
    Path: string; 
    Size: Int64; 
    IsDuplicate: Boolean; 
  end; 

var 
  FileList: array of TFileData; 
  FilesCount: Integer = 0; 

// 1. Рекурсивный поиск файлов
procedure ScanDirectory(const TargetDir: string);
var 
  SearchRec: TSearchRec; // ИСПРАВЛЕНО: было ";" стало ":"
begin
  // Начинаем поиск всех файлов в директории 
  if FindFirst(TargetDir + '*', faAnyFile, SearchRec) = 0 then 
  begin 
    try
      repeat 
        // Пропускаем системные указатели на текущую и родительскую папки 
        if (SearchRec.Name <> '.') and (SearchRec.Name <> '..') then 
        begin 
          // Если это папка - идем внутрь 
          if (SearchRec.Attr and faDirectory) <> 0 then 
            ScanDirectory(TargetDir + SearchRec.Name + DirectorySeparator)
          else
          begin 
            // Если это файл - сохраняем данные в массив 
            SetLength(FileList, FilesCount + 1); 
            FileList[FilesCount].Path := TargetDir + SearchRec.Name;
            FileList[FilesCount].Size := SearchRec.Size;
            FileList[FilesCount].IsDuplicate := False; 
            Inc(FilesCount); 
          end;
        end;
      until FindNext(SearchRec) <> 0; 
    finally
      FindClose(SearchRec); // Освобождаем ресурсы поиска
    end;
  end;
end;

// 2. Побайтовое сравнение содержимого
function CompareFileContent(const Path1, Path2: string): Boolean;
var 
  F1, F2: TFileStream;
  Buf1, Buf2: array[1..8192] of Byte; 
  BytesRead: Integer;
begin
  Result := False; 
  try
    F1 := TFileStream.Create(Path1, fmOpenRead or fmShareDenyNone);
    try
      F2 := TFileStream.Create(Path2, fmOpenRead or fmShareDenyNone);
      try 
        if F1.Size <> F2.Size then Exit; 

        while F1.Position < F1.Size do 
        begin 
          BytesRead := F1.Read(Buf1, SizeOf(Buf1));
          F2.Read(Buf2, SizeOf(Buf2));
          if not CompareMem(@Buf1, @Buf2, BytesRead) then Exit;
        end;
        Result := True; 
      finally
        F2.Free; 
      end;
    finally
      F1.Free; 
    end;
  except
    Result := False;
  end;
end;

var 
  i, j: Integer;
  Temp: TFileData;
  Answer: string;

begin 
  WriteLn('___ Welcome to Pascal Duplicate Hunter ___');
  WriteLn('Enter the path to folder:');
  ReadLn(Answer);

  if (Answer <> '') and (Answer[Length(Answer)] <> DirectorySeparator) then 
    Answer := Answer + DirectorySeparator;

  WriteLn('Step 1: Scanning...'); 
  ScanDirectory(Answer);
  WriteLn('Files found: ', FilesCount);

  // Сортировка по размеру для ускорения
  for i := 0 to FilesCount - 2 do
    for j := 0 to FilesCount - 2 - i do
      if FileList[j].Size > FileList[j+1].Size then
      begin
        Temp := FileList[j];
        FileList[j] := FileList[j+1];
        FileList[j+1] := Temp;
      end;

  // Поиск дублей
  for i := 0 to FilesCount - 2 do
  begin
    if (FileList[i].IsDuplicate) then Continue;
    
    j := i + 1;
    while (j < FilesCount) and (FileList[i].Size = FileList[j].Size) do
    begin
      if CompareFileContent(FileList[i].Path, FileList[j].Path) then
      begin
        FileList[j].IsDuplicate := True;
        WriteLn('Duplicate found: ', FileList[j].Path);
      end;
      Inc(j);
    end;
  end;

  WriteLn('Done. Delete duplicates? (Y/N)');
  ReadLn(Answer);
  if UpperCase(Answer) = 'Y' then
  begin
    for i := 0 to FilesCount - 1 do
      if FileList[i].IsDuplicate then DeleteFile(FileList[i].Path);
    WriteLn('Cleaned up!');
  end;
end.
