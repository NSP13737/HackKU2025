
export const mockOfficers = [
  "Officer #1",
  "Officer #2",
  "Officer #3",
  "Officer #4"
];

export const mockFiles = [
  {
    id: "summary1",
    name: "Summary #1",
    date: "2025-04-01",
    officerId: "Officer #1",
    content: "This is the first summary of Officer #1's bodycam footage.\n\nDuring the incident, the officer approached the vehicle with caution after observing erratic driving behavior. The driver was cooperative and provided identification when requested.\n\nThe officer explained the reason for the stop clearly and maintained a professional demeanor throughout the interaction."
  },
  {
    id: "summary2",
    name: "Summary #2",
    date: "2025-04-02",
    officerId: "Officer #1",
    content: "This is the second summary of Officer #1's bodycam footage.\n\nThe officer responded to a noise complaint at a residential address. Upon arrival, the officer spoke with the homeowner and explained the complaint.\n\nThe interaction was brief and ended with the homeowner agreeing to lower the volume of music. The officer provided their badge number when requested."
  },
  {
    id: "summary3",
    name: "Summary #3",
    date: "2025-04-03",
    officerId: "Officer #1",
    content: "This is the third summary of Officer #1's bodycam footage.\n\nThe officer conducted a routine patrol in a high-traffic area. Several pedestrians were advised about jaywalking regulations.\n\nThe officer demonstrated good community engagement by answering questions from citizens about local traffic laws."
  },
  {
    id: "summary4",
    name: "Summary #4",
    date: "2025-04-04",
    officerId: "Officer #1",
    content: "This is the fourth summary of Officer #1's bodycam footage.\n\nThe officer assisted a stranded motorist with a disabled vehicle. The officer helped arrange for towing services and ensured the motorist was safely off the road.\n\nThe interaction demonstrated good community service practices and attention to public safety."
  },
  {
    id: "summary5",
    name: "Summary #1",
    date: "2025-04-01",
    officerId: "Officer #2",
    content: "This is the first summary of Officer #2's bodycam footage.\n\nThe officer conducted a traffic stop for a vehicle with expired registration. The driver was informed of the violation and issued a warning.\n\nThe officer provided clear instructions and information about how to renew vehicle registration online."
  },
  {
    id: "summary6",
    name: "Summary #2",
    date: "2025-04-02",
    officerId: "Officer #2",
    content: "This is the second summary of Officer #2's bodycam footage.\n\nThe officer responded to a shoplifting incident at a local store. The officer interviewed the store manager and reviewed security footage.\n\nThe suspect was identified and appropriate documentation was completed. The officer maintained professionalism throughout the process."
  }
];

// Function to simulate fetching data
export const fetchOfficerFiles = (officerId: string) => {
  return mockFiles.filter(file => file.officerId === officerId);
};

export const fetchFileSummary = (fileId: string) => {
  const file = mockFiles.find(file => file.id === fileId);
  
  if (!file) {
    return null;
  }
  
  return {
    title: `Summary for ${file.name}`,
    content: file.content
  };
};
