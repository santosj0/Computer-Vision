function myOutput = skeleton(image,disk)
%SKELETON
%Generates a skelatal image based off of a specified disk
%
% Array Index
index = 1;
myOutput = skelSubSet(image,disk,0);
while (isSkelEmpty(skelSubSet(image,disk,index)) ~= 1)
    myOutput = myOutput + skelSubSet(image,disk,index);
    index = index + 1;
end
myOutput = logical(myOutput);
end

