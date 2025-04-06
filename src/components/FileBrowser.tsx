
import React from 'react';
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { FileText } from "lucide-react";
import { cn } from "@/lib/utils";

interface FileItem {
  id: string;
  name: string;
  date: string;
}

interface FileBrowserProps {
  files: FileItem[];
  selectedFile: string | null;
  onSelectFile: (fileId: string) => void;
}

export const FileBrowser: React.FC<FileBrowserProps> = ({
  files,
  selectedFile,
  onSelectFile
}) => {
  return (
    <div className="h-full flex flex-col border-2 border-police-border rounded-md">
      <div className="p-3 bg-police-blue text-white font-semibold border-b border-police-border">
        File Layout
      </div>
      
      <ScrollArea className="flex-1">
        <div className="p-2 space-y-2">
          {files.map((file) => (
            <Button
              key={file.id}
              variant="ghost"
              className={cn(
                "w-full justify-start gap-2 p-2 h-auto border border-gray-200",
                selectedFile === file.id ? "bg-police-light border-police-border" : ""
              )}
              onClick={() => onSelectFile(file.id)}
            >
              <FileText className="h-4 w-4 shrink-0" />
              <div className="flex flex-col items-start">
                <span className="font-medium">{file.name}</span>
                <span className="text-xs text-muted-foreground">{file.date}</span>
              </div>
            </Button>
          ))}
        </div>
      </ScrollArea>
    </div>
  );
};
