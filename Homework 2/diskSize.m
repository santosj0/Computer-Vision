function myOutput = diskSize(disk,size)
%DISKSIZE Summary of this function goes here
%   Detailed explanation goes here
if(size > 1)
    myOutput = imdilate(disk,disk);
    for x = 1:(size-2)
        myOutput = imdilate(myOutput,disk);
    end
elseif (size == 1)
        myOutput = disk;
else
    myOutput = [0 0 0; 0 1 0; 0 0 0];
end
end

