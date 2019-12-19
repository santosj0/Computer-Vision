function myOutput = skelSubSet(image,disk,size)
%SKELSUBSET Summary of this function goes here
%   Detailed explanation goes here
d = diskSize2(disk,size);
if size == 0
    myOutput = image - imopen(image,disk);
else
    myOutput = imerode(image,d) &~ imopen(imerode(image,d),disk);
end
end

