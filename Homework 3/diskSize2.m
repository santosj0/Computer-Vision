function myOutput = diskSize2(disk, size1)
%DISKSIZE2 Summary of this function goes here
%   Detailed explanation goes here

if(size1 > 1)
    myOutput = disk;
    for x = 1:(size1-1)
        myOutput = padarray(myOutput,[2,2],0,'both');
        myOutput = imdilate(myOutput,disk);
    end
elseif (size1 == 1)
        myOutput = disk;
else
    myOutput = [0 0 0; 0 1 0; 0 0 0];
end

myOutput = logical(myOutput);

end

