function myOutput = createDisk(image)
%CREATEDISK Summary of this function goes here
%   Detailed explanation goes here
[c,r] = size(image);
if(c >= 3 && r >= 4)
    myOutput = zeros(c,r);
    myOutput(floor(c/2),floor(r/2)) = 1;
    myOutput(floor(c/2),floor(r/2)-1) = 1;
    myOutput(floor(c/2),floor(r/2)+1) = 1;
    myOutput(floor(c/2),floor(r/2)+2) = 1;
    myOutput(floor(c/2)-1,floor(r/2)) = 1;
    myOutput(floor(c/2)-1,floor(r/2)+1) = 1;
    myOutput(floor(c/2)-1,floor(r/2)-1) = 1;
    myOutput(floor(c/2)-1,floor(r/2)+2) = 1;
    myOutput(floor(c/2)-2,floor(r/2)) = 1;
    myOutput(floor(c/2)-2,floor(r/2)+1) = 1;
    myOutput(floor(c/2)+1, floor(r/2)) = 1;
    myOutput(floor(c/2)+1, floor(r/2)+1) = 1;
else
    myOutput = 0;
end
end

