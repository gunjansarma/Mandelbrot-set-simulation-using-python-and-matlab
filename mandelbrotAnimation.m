function mandelbrotAnimation
    % Parameters
    width = 800;        % Width of the image
    height = 800;       % Height of the image
    max_iterations = 100; % Maximum number of iterations

    % Define the region of interest in the complex plane
    xmin = -2;
    xmax = 1;
    ymin = -1.5;
    ymax = 1.5;

    % Generate an evenly spaced grid in the specified region
    [X, Y] = meshgrid(linspace(xmin, xmax, width), linspace(ymin, ymax, height));

    % Create a figure for the animation
    figure;

    % Loop through frames
    for frame = 1:max_iterations
        % Compute the Mandelbrot set for each point in the grid
        Z = mandelbrot(X + 1i * Y, max_iterations);

        % Plot the Mandelbrot set
        imagesc([xmin, xmax], [ymin, ymax], frame + log(abs(Z)), [1, max_iterations + log(max_iterations)]);
        colormap(hot);
        colorbar;
        title(['Mandelbrot Set Animation (Frame ' num2str(frame) '/' num2str(max_iterations) ')']);
        xlabel('Re(z)');
        ylabel('Im(z)');

        % Pause to control the animation speed
        pause(0.1);

        % Clear the previous plot
        clf;
    end
end

function Z = mandelbrot(C, max_iterations)
    % Mandelbrot set computation
    Z = zeros(size(C));
    for k = 1:max_iterations
        Z = Z.^2 + C;
    end
end
