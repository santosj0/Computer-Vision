function myOutput = reconstruction(imageArr,disk)
%RECONSTRUCTION Summary of this function goes here
%   Detailed explanation goes here
size1 = size(imageArr);
myOutput = imageArr(:,:,1);
for x = 2:size1(3)
    myOutput = myOutput + imdilate(imageArr(:,:,x),diskSize2(disk,x-1));
end
myOutput = logical(myOutput);
end

