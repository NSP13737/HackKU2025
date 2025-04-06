
import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";

interface SummaryViewProps {
  selectedFile: string | null;
  summaryData: {
    content: string;
    title: string;
  } | null;
  isLoading: boolean;
}

export const SummaryView: React.FC<SummaryViewProps> = ({
  selectedFile,
  summaryData,
  isLoading
}) => {
  return (
    <Card className="h-full border-2 border-police-border">
      <CardHeader className="border-b border-gray-200 pb-3">
        <CardTitle className="text-xl font-semibold">
          {isLoading ? (
            <Skeleton className="h-6 w-3/4" />
          ) : summaryData ? (
            summaryData.title
          ) : (
            "Select a file to view summary"
          )}
        </CardTitle>
      </CardHeader>
      <CardContent className="p-4 h-[calc(100%-4rem)] overflow-auto">
        {isLoading ? (
          <div className="space-y-2">
            <Skeleton className="h-4 w-full" />
            <Skeleton className="h-4 w-full" />
            <Skeleton className="h-4 w-3/4" />
          </div>
        ) : summaryData ? (
          <div className="whitespace-pre-line">{summaryData.content}</div>
        ) : (
          <div className="flex items-center justify-center h-full text-muted-foreground">
            {selectedFile ? "Loading summary..." : "No file selected"}
          </div>
        )}
      </CardContent>
    </Card>
  );
};
