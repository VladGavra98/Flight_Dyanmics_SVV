load("matlab.mat")
AoA_tab=flightdata.vane_AOA.data;
fields = fieldnames(flightdata);
directory = "C:\Users\vladg\OneDrive\Documents\BSc_AE_III\Simulation, Verification, Validation\FD\Data\";
for i = 1:numel(fields)
  current = flightdata.(fields{i});
  

  tab = current.data;
  name = fields{i};
  disp(current);
  filename = string(directory + string(fields{i})+".txt");
  T = table(tab);
  
  
  writetable(T,filename);

end

   
    
