function myOutput = isSkelEmpty(image)
%ISSKELEMPTY Summary of this function goes here
%   Detailed explanation goes here
[y,x] = size(image);
myOutput = 1;
for a = 1:y
    for b = 1:x
        if (image(a,b) == 1)
            myOutput = 0;
            break
        end
    end
    if(myOutput == 0)
        break
    end
end
end

