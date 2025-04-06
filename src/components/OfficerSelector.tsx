
import React from 'react';
import { Button } from "@/components/ui/button";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { ChevronLeft, ChevronRight } from "lucide-react";

interface OfficerSelectorProps {
  currentOfficer: string;
  setCurrentOfficer: (officer: string) => void;
  officers: string[];
}

export const OfficerSelector: React.FC<OfficerSelectorProps> = ({
  currentOfficer,
  setCurrentOfficer,
  officers
}) => {
  const currentIndex = officers.indexOf(currentOfficer);
  
  const handlePrevious = () => {
    const newIndex = (currentIndex - 1 + officers.length) % officers.length;
    setCurrentOfficer(officers[newIndex]);
  };
  
  const handleNext = () => {
    const newIndex = (currentIndex + 1) % officers.length;
    setCurrentOfficer(officers[newIndex]);
  };
  
  return (
    <div className="flex items-center justify-between w-full gap-2 p-4 border-2 border-police-border bg-white rounded-md">
      <Button 
        variant="outline" 
        size="icon" 
        onClick={handlePrevious}
        className="border-police-border"
      >
        <ChevronLeft className="h-4 w-4" />
      </Button>
      
      <div className="flex-1">
        <Select value={currentOfficer} onValueChange={setCurrentOfficer}>
          <SelectTrigger className="w-full text-xl font-semibold">
            <SelectValue placeholder="Select Officer" />
          </SelectTrigger>
          <SelectContent>
            {officers.map((officer) => (
              <SelectItem key={officer} value={officer}>
                {officer}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>
      
      <Button 
        variant="outline" 
        size="icon"
        onClick={handleNext}
        className="border-police-border"
      >
        <ChevronRight className="h-4 w-4" />
      </Button>
    </div>
  );
};
