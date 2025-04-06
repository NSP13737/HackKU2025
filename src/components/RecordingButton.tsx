
import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Mic, Square } from "lucide-react";
import { useToast } from "@/components/ui/use-toast";

interface RecordingButtonProps {
  onRecordingComplete: (recordingName: string) => void;
}

export const RecordingButton: React.FC<RecordingButtonProps> = ({ onRecordingComplete }) => {
  const [isRecording, setIsRecording] = useState(false);
  const [recordingTime, setRecordingTime] = useState(0);
  const { toast } = useToast();
  
  const toggleRecording = () => {
    if (isRecording) {
      // Simulate recording completion
      stopRecording();
    } else {
      // Start new recording
      startRecording();
    }
  };
  
  const startRecording = () => {
    setIsRecording(true);
    setRecordingTime(0);
    
    toast({
      title: "Recording started",
      description: "Your new session is now being recorded.",
    });
    
    // Simulate timer
    const interval = setInterval(() => {
      setRecordingTime(prev => prev + 1);
    }, 1000);
    
    // Store interval ID in component
    (window as any).recordingInterval = interval;
  };
  
  const stopRecording = () => {
    setIsRecording(false);
    clearInterval((window as any).recordingInterval);
    
    const currentDate = new Date();
    const recordingName = `Recording_${currentDate.toISOString().slice(0, 10).replace(/-/g, '')}_${currentDate.getHours()}${currentDate.getMinutes()}`;
    
    toast({
      title: "Recording completed",
      description: `Your ${formatTime(recordingTime)} recording has been saved.`,
    });
    
    onRecordingComplete(recordingName);
  };
  
  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };
  
  return (
    <div className="p-4 border-t-2 border-police-border bg-white">
      <Button
        variant={isRecording ? "destructive" : "default"}
        className={`w-full py-6 text-xl font-bold ${!isRecording ? "bg-police-blue hover:bg-police-accent" : ""}`}
        onClick={toggleRecording}
      >
        {isRecording ? (
          <>
            <Square className="h-5 w-5 mr-2" /> Stop Recording ({formatTime(recordingTime)})
          </>
        ) : (
          <>
            <Mic className="h-5 w-5 mr-2" /> New Recording
          </>
        )}
      </Button>
    </div>
  );
};
