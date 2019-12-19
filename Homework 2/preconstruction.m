function myOutput = preconstruction(imageArr,disk,desize)
% This function will take an array of binary skeleton
% subsets as well as its corresponding disk and a desired
% size, and combine those subsets from the biggest Sn until
% the desired size. If desired size is greater than the skeleton 
% subsets then it will return the greatest subset. If the desired
% size is 0, then it will return the reconstruction of the image.
    size1 = size(imageArr);
    size3 = size1(3);
    if (desize == 0)
        myOutput = reconstruction(imageArr,disk);
    elseif (desize >= size3)
        myOutput = imdilate(imageArr(:,:,size3),diskSize2(disk,size3));
    else
        myOutput = imdilate(imageArr(:,:,size3),diskSize2(disk,size3-1));
        for x = size1(3)-1:-1:desize+1
            myOutput = myOutput + imdilate(imageArr(:,:,x),diskSize2(disk,x-1));
        end
    end
    myOutput = logical(myOutput);
end

