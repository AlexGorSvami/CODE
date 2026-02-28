Program DuplicateHunter;
//Directives for compilator: use modern syntax(ObjectPascal) and on support AnsiString
{$mode objfpc}{$H+}

uses
    SysUtils, //work with file system and time 
    Classes; //Work with TfileStream and lists 

type
    //Structure for storage data about file 
    TfileData = record 
     Path: string; //full path to file 
     Size: Int64; //Size in byte(Int64 for support > 4Gb)
     IsDuplicate: Boolean; //Label for duplicate 
    end; 

var 
    FileList: array of TfileData; //Dynamic array for all found files 
    FilesCount: Integer = 0; //Counter for found files 

//  1.Resursive research files 
procedure ScanDirectory(const TargetDir: string);
var 
    SearchRec; TSearchRec; //Special structure for storage data
begin
    //Start search all files in directory 
    if FindFirst(TargetDir + '*', faAnyFile, SearchRec) = 0 then 
    begin 
        repeat 
            //Scip system pointer in this and parent folder 
            if (SearchRec.Name <> '.') and (SearchRec.Name <> '..') then 
            begin 
                // If this is folder - let's go inside 
                if (SearchRec.Attr and faDirectory) <> 0 then 
                    ScanDirectory(TargetDir + SearchRec.Name + DirectorySeparator)
                else
                begin 
                    //It it's file save data to array 
                    SetLength(FileList, FilesCount + 1); 
                    FileList[FilesCount].Path := TargetDir + SearchRec.Name;
                    FileList[FilesCount].Size := SearchRec.Size;
                    FileList[FilesCount].IsDuplicate := False; 
                    Inc(FilesCount); //Increase the counter 
                end;
            end;
            until FindNext(SearchRec) <> 0; //Find next file, untill they run out 
            FindClose(SearchRec); //Must free up search resources 
        end;
    end;
//Byte-by-byte compresion 
function CompareFileContent(const Path1, Path2: string): Boolean;
var 
    F1, F2: TfileStream;
    Buf1, Buf2: array[1..8192] of Byte; //Buffer 8Kb for fast clean
    BytesRead: Integer;
begin
    Result := False; //by default consider files to be different
    try
        // Open both files only read 
        F1 := TfileStream.Create(Path1, fmOpenRead or fmShareDenyNone);
        F2 := TfileStream.Create(Path2, fmOpenRead or fmShareDenyNone);
        try 
        //If the sides aren't equal, exit
        if F1.Size <> F2.Size then Exit; 

        //Read files in portions, untill we get the finish 
        while F1.Position < F1.Size do 
        begin 
            BytesRead := F1.Read(Buf1, SizeOf(Buf1));
            F2.Read(Buf2, SizeOf(Buf2));

            //Comparing areas and buffers 
            if not CompareMem(@Buf1, @Buf2, BytesRead) then Exit;
        end;
        Result := True; //If we go to this - files identical
    finally
        F1.Free; //Closing files 
        F2.Free; 
    end;
  except
    //If the file busy with another program 
    Result := False;
  end;
end;

var 
    i, j: Integer;
    Temp: TFileData;
    Answer: string;

begin 
    Writeln('___Welcome to Pascal Duplicate Hunter ___');
    Writeln('Enter the path to folder (example, C:\MyFiles\):');
    ReadLn(Answer);

    //Add a slash in the end if you forgot it 
    if (Answer <> '') and (Answer[Length(Answer)]) <> DirectorySeparator) then 
        Answer := Answer + DirectorySeparator;

    Writeln('Step 1: Scan the folder...'); 
    ScanDirectory(Answer);
    Writeln('Find files: ', FilesCount);
    

