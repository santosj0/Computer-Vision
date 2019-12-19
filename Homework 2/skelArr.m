function myOutput = skelArr(image,disk)
%SKELARR Summary of this function goes here
%   Detailed explanation goes here
index = 1;
myOutput(:,:,1) = skelSubSet(image,disk,0);
while isSkelEmpty(skelSubSet(image,disk,index)) ~= 1
    myOutput(:,:,index+1) = skelSubSet(image,disk,index);
    index = index + 1;
end
myOutput = logical(myOutput);
end

