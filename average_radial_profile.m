clc;    % Clear the command window.
close all;  % Close all figures (except those of imtool.)
clear;  % Erase all existing variables. Or clearvars if you want.
workspace;  % Make sure the workspace panel is showing.
format long g;
format compact;
fontSize = 20;

% Create some sample data.
[X,Y,grayImage] = peaks(330);
grayImage = uint8(255 * mat2gray(grayImage));
% Display the original image.
subplot(2, 3, 1);
imshow(grayImage, []);
axis on;
title('Original Image', 'FontSize', fontSize);
set(gcf, 'units','normalized','outerposition',[0 0 1 1]); % Maximize figure.

% Let's compute and display the histogram.
[pixelCount, grayLevels] = imhist(grayImage);
subplot(2, 3, 2); 
bar(grayLevels, pixelCount);
grid on;
title('Histogram of Original Image', 'FontSize', fontSize);
xlim([0 grayLevels(end)]); % Scale x axis manually.

% Binarize it to find bright things, such as the dike.
binaryImage = grayImage > 160;
% Display the image.
subplot(2, 3, 3);
imshow(binaryImage, []);
title('Binarized', 'FontSize', fontSize);
drawnow;

% Compute the Euclidean Distance Transform
edtImage = bwdist(binaryImage);
% Display the image.
subplot(2, 3, 4);
imshow(edtImage, []);
title('Euclidean Distance Transform', 'FontSize', fontSize);

% Get the histogram of it so we know what distances are there
% allDistances = unique(edtImage)
maxDistance = ceil(max(edtImage(:)))

% Let's compute and display the histogram.
[pixelCounts, binCenters] = hist(edtImage(:), 100);
subplot(2, 3, 5); 
bar(binCenters, pixelCounts);
grid on;
title('Histogram of EDT image', 'FontSize', fontSize);
xlim([0 binCenters(end)]); % Scale x axis manually.

% Allocate an array for the profile
profileSums = zeros(1, maxDistance);
profileCounts = zeros(1, maxDistance);
% Scan the original image getting gray level, and scan edtImage getting distance.
% Then add those values to the profile.
[rows, columns] = size(edtImage);
for column = 1 : columns
	for row = 1 : rows
		thisDistance = round(edtImage(row, column));
		if thisDistance <= 0
			continue;
		end
		profileSums(thisDistance) = profileSums(thisDistance) + double(grayImage(row, column));
		profileCounts(thisDistance) = profileCounts(thisDistance) + 1;
	end
end
% Divide the sums by the counts at each distance to get the average profile
averageRadialProfile = profileSums ./ profileCounts;
subplot(2, 3, 6); 
plot(1:length(averageRadialProfile), averageRadialProfile, 'b-', 'LineWidth', 3);
grid on;
title('Average Radial Profile', 'FontSize', fontSize);
xlabel('Distance from nearest white region', 'FontSize', fontSize);
ylabel('Gray Level', 'FontSize', fontSize);
