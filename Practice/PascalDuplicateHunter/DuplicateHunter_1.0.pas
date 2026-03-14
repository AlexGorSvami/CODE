program DuplicateHunter;

{$mode objfpc}{$H+}

uses
  SysUtils, Classes;

type
  TFileData = record
    Path: string;
    Size: Int64;
    IsDuplicate: Boolean;
  end;

var
  FileList: array of TFileData;
  FilesCount: Integer = 0;

// 1. Recursive folder scan
procedure ScanDirectory(const TargetDir: string);
var
  SearchRec: TSearchRec;
begin
  if FindFirst(TargetDir + '*', faAnyFile, SearchRec) = 0 then
  begin
    try
      repeat
        // Skip current/parent dir pointers
        if (SearchRec.Name <> '.') and (SearchRec.Name <> '..') then
        begin
          // If directory, scan it
          if (SearchRec.Attr and faDirectory) <> 0 then
            ScanDirectory(TargetDir + SearchRec.Name + DirectorySeparator)
          else
          begin
            // If file, save to array
            SetLength(FileList, FilesCount + 1);
            FileList[FilesCount].Path := TargetDir + SearchRec.Name;
            FileList[FilesCount].Size := SearchRec.Size;
            FileList[FilesCount].IsDuplicate := False;
            Inc(FilesCount);
          end;
        end;
      until FindNext(SearchRec) <> 0;
    finally
      FindClose(SearchRec); // Free resources
    end;
  end;
end;

// 2. Byte-by-byte content comparison
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
        // Different size -> not duplicates
        if F1.Size <> F2.Size then Exit;

        // Read and compare chunks
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
    Result := False; // On read error
  end;
end;




var 
    i, j: Integer;
    Temp: TFileData;
    Answer: string;

begin 
    Writeln('___Pascal Duplicate Hunter 1.0 ___');

    //If an argument is passed, we take it; otherwise, we take the current folder
    if ParamCount > 0 then
        Answer := ParamStr(1)
    else
        Answer := GetCurrentDir;

    //Mandatory slash at the end 
    if (Length(Answer) > 0) and (Answer[Length(Answer)] <> DirectorySeparator) then 
        Answer := Answer + DirectorySeparator;

    //Checking the existence of a directory 
    if not DirectoryExists(Answer) then 
    begin 
        Writeln('ERROR: Directory not found: ', Answer);
        Exit;
    end;

    Writeln('Scanning directory: ', Answer);
    ScanDirectory(Answer);

    if FilesCount = 0 then 
    begin 
        Writeln('Directory is empty. No files to scan.');
        Exit;
    end;

    Writeln('Files found: ', FilesCount);

    //Sort by size 
    for i := 0 to FilesCount - 2 do 
    begin
        for j := 0 to FilesCount - 2 - i do 
            if FileList[j].Size > FileList[j+1].Size then 
            begin 
                Temp := FileList[j];
                FileList[j] := FileList[j+1];
                FileList[j+1] := Temp;
            end;
    end;
    // Search duplicate 
    for i := 0 to FilesCount - 2 do 
    begin 
        if FileList[i].IsDuplicate then Continue;
        j := i + 1;
        while (j < FilesCount) and (FileList[i].Size = FileList[j].Size) do 
        begin 
            if CompareFileContent(FileList[i].Path, FileList[j].Path) then 
            begin 
                FileList[j].IsDuplicate := True;
                Writeln('Duplicate found: ', FileList[j].Path);
            end;
            Inc(j);
        end;
    end;

    //Request for deletion 
    Writeln('Done. Delete duplicates? (Y\N)');
    ReadLn(Answer);
    if UpperCase(Answer) = 'Y' then 
    begin 
        for i := 0 to FilesCount - 1 do 
            if FileList[i].IsDuplicate then DeleteFile(FileList[i].Path);
        Writeln('Clean up!');
    end;
end.
