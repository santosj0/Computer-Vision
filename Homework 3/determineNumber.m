function [outputArg1] = determineNumber(image)
%DETERMINENUMBER: Purpose of this function is to take in a binary image and
%then determine which number that binary image represents. If no answer is
%provided, then it rotates the image and tries again until degrees is 360.

%First we get the features of that image
%[holes,tll,trl,bll,brl]
result = determineFeatures(image);
totall = result(2) + result(3) + result(4) + result(5);

%Start of the tree determining factor
%Possible answers: 8
if(result(1) > 1 )
    outputArg1 = 'eight';
    
%Posible answers: 0, 4, 6, 9
elseif (result(1) == 1)
    %Possible answers: 0
    if(totall == 0)
        outputArg1 = 'zero';
    
    %Possible answers: 4
    elseif(totall > 1)
        outputArg1 = 'four';
    
    %Possible answers: 6, 9
    else
        
        %Possible answers: 6
        if(result(3) >= 1)
            outputArg1 = 'six';
        
        %Possible answers: 9
        else
            outputArg1 = 'nine';
        end
        
    end

%Possible answers: 1, 2, 3, 5, 7
else
    
    %Possible answers: 3
    if(totall > 2)
        outputArg1 = 'three';
    
    %Possible answers: 7
    elseif(totall < 2)
        outputArg1 = 'seven';
        
    %Possible answers: 1, 2, 5    
    else
        
        %Possible answers: 2
        if(result(2) == 1 && result(5) == 1)
            outputArg1 = 'two';
            
        %Possible answers: 5    
        elseif (result(3) == 1 && result(4) == 1)
            outputArg1 = 'five';
            
        %Possible answers: 1
        else
            outputArg1 = 'one';
            
        end
        
    end
    
end


end

