
import React, { useState, useEffect } from 'react';
import { OfficerSelector } from "@/components/OfficerSelector";
import { FileBrowser } from "@/components/FileBrowser";
import { SummaryView } from "@/components/SummaryView";
import { RecordingButton } from "@/components/RecordingButton";
import { mockOfficers, fetchOfficerFiles, fetchFileSummary } from "@/lib/mockData";
import { toast } from "@/components/ui/use-toast";

const Index = () => {
  const [currentOfficer, setCurrentOfficer] = useState(mockOfficers[0]);
  const [officerFiles, setOfficerFiles] = useState<any[]>([]);
  const [selectedFile, setSelectedFile] = useState<string | null>(null);
  const [summaryData, setSummaryData] = useState<any | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  // Load officer files when current officer changes
  useEffect(() => {
    const files = fetchOfficerFiles(currentOfficer);
    setOfficerFiles(files);
    setSelectedFile(files.length > 0 ? files[0].id : null);
  }, [currentOfficer]);

  // Load summary when selected file changes
  useEffect(() => {
    if (selectedFile) {
      setIsLoading(true);
      
      // Simulate API call delay
      setTimeout(() => {
        const summary = fetchFileSummary(selectedFile);
        setSummaryData(summary);
        setIsLoading(false);
      }, 800);
    } else {
      setSummaryData(null);
    }
  }, [selectedFile]);

  const handleSelectFile = (fileId: string) => {
    setSelectedFile(fileId);
  };

  const handleRecordingComplete = (recordingName: string) => {
    toast({
      title: "Processing recording",
      description: "Your recording is being transcribed and analyzed.",
    });
    
    // Simulate a new recording being processed and added
    setTimeout(() => {
      toast({
        title: "Recording processed",
        description: "Your new recording has been analyzed and added to the files.",
      });
      
      // Refresh the file list
      const files = fetchOfficerFiles(currentOfficer);
      setOfficerFiles(files);
    }, 3000);
  };

  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <main className="flex-1 container py-4 grid grid-cols-4 gap-4 max-w-7xl">
        {/* Left column - Officer selector and Summary view */}
        <div className="col-span-3 flex flex-col gap-4">
          <OfficerSelector 
            currentOfficer={currentOfficer} 
            setCurrentOfficer={setCurrentOfficer} 
            officers={mockOfficers} 
          />
          
          <div className="flex-1">
            <SummaryView 
              selectedFile={selectedFile} 
              summaryData={summaryData} 
              isLoading={isLoading} 
            />
          </div>
          
          <RecordingButton onRecordingComplete={handleRecordingComplete} />
        </div>
        
        {/* Right column - File browser */}
        <div className="col-span-1 h-full">
          <FileBrowser 
            files={officerFiles} 
            selectedFile={selectedFile} 
            onSelectFile={handleSelectFile} 
          />
        </div>
      </main>
    </div>
  );
};

export default Index;
