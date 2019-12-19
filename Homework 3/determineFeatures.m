function [outputArg] = determineFeatures(image)
%DETERMINEFEATURES: The purpose of this function is to
%determine how many lids and holes an image input has
%based on the disk [0 1 1 0; 1 1 1 1; 1 1 1 1; 0 1 1 0].
%This function will output an array where index 1 is the number
%of holes, index 2 is the number of top left lids, index 3 is
%the number of top right lids, index 4 is number of bottom left lids,
% and index 5 is number of bottom right lids.

%First close the image with disk to sort of clean the image
disk = [ 0 1 1 0; 1 1 1 1; 1 1 1 1; 0 1 1 0];
image = imclose(image,disk);

%Next we dilate the disk 7 times to get the disk as 7B
disk7 = diskSize2(disk,7);

%Now we close the orignal image with the 7B disk
close = imclose(image,disk7);

%Take the set difference between the closed image and original image
result1 = close &~ image;

%Now we dilate with [1 1 1; 1 1 1; 1 1 1] and then set diff with closed
%image
result2 = imdilate(result1,[1 1 1; 1 1 1; 1 1 1]) &~ close;

%We use regionprops to get the centroid of the components and original
%image
stats1 = regionprops(result2,'centroid');
r = size(stats1);
stats2 = regionprops(image,'centroid');

%Now we count the number of tleft/tright/bleft/bright lids
tll = 0;
trl = 0;
bll = 0;
brl = 0;

%Can get more specific based on location
%For example, seperate the image into 9 quadrants
for x=1:r(1)
    %++
    if(stats1(x).Centroid(1) > stats2.Centroid(1) && stats1(x).Centroid(2) > stats2.Centroid(2))
        brl = brl + 1;
    %-+
    elseif(stats1(x).Centroid(1) < stats2.Centroid(1) && stats1(x).Centroid(2) > stats2.Centroid(2))
        bll = bll + 1;
    %+-
    elseif(stats1(x).Centroid(1) > stats2.Centroid(1) && stats1(x).Centroid(2) < stats2.Centroid(2))
        trl = trl + 1;
    %--
    elseif(stats1(x).Centroid(1) < stats2.Centroid(1) && stats1(x).Centroid(2) < stats2.Centroid(2))
        tll = tll + 1;
    end
end

%Now we count the difference in lids and components to get holes
label1 = bwlabel(result1);
h1 = bwconncomp(label1);
label2 = bwlabel(result2);
h2 = bwconncomp(label2);
holes = h1.NumObjects - h2.NumObjects;

%We create a check to see if the image centroid is inside the image
%isc = false;
%rc = round(stats2.Centroid);
%if (image(rc(2),rc(1)) == 1)
%    isc = true;
%end

%Now we return the number of holes, leftlids, and rightlids
outputArg = [holes,tll,trl,bll,brl];

end

