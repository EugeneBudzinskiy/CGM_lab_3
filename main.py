from PIL import Image, ImageDraw
from numpy import ones, multiply

from CellFinder import CellFinder                        # Import Class of Cell Finder algorithm


def main():
    filename = 'DS1.txt'                                 # Name of dataset file
    result_filename = 'result.png'                       # Name of result file
    canvas_size = (540, 960)                             # Canvas size of image

    cell_finder = CellFinder()                           # Init of CellFinder

    with open(filename) as file:                         # Work with file
        canvas_size_ext = canvas_size + tuple([3])       # Add RGB-mask part
        mask = ones(canvas_size_ext, dtype='uint8')      # Create numpy array fill with ones

        file_array = file.read()                         # Read all data from file in to array
        file_array = file_array[:-1]                     # Delete last '\n' from array
        file_array = file_array.split('\n')              # Split coordination by '\n'

        coords = [x.split(' ') for x in file_array]      # Split coord from 1d array to 2 2d array
        coords = [[int(y) for y in x] for x in coords]   # Convert str coord to int coord

        for coord_x, coord_y in coords:                  # Work with coordination's
            mask[coord_x, coord_y] = [0, 0, 0]           # Change color of right pixels to black

        image = multiply(mask, 255)                      # Scale data from [0, 1] to [0, 255]
        image = Image.fromarray(image)                   # Create image from data array
        image = image.transpose(Image.FLIP_TOP_BOTTOM)   # Flip the image

        image.show()                                     # Show result without cell
        image.save(result_filename)                      # Save the result image

        image = image.transpose(Image.FLIP_TOP_BOTTOM)   # Flip back the image for cell
        draw = ImageDraw.Draw(image)                     # Create a drawing tool

        cell_result = cell_finder.process(coords)        # Run the cell finder
        ln = len(cell_result)                            # Get len of result cell list

        for i in range(ln):                              # Run throw all point of cell
            start_line = cell_result[i]                  # Init the start line position in 'coords'

            if i == ln - 1:                              # if last point of cell
                end_line = cell_result[0]                # Close the cell
            else:
                end_line = cell_result[i + 1]            # Choose the next point of cell

            start_x, start_y = coords[start_line]        # Convert position in 'coords' in to real coords
            end_x, end_y = coords[end_line]              # Same for end of line

            draw.line((start_y, start_x, end_y, end_x),  # Draw the line where is need
                      fill=(0, 191, 255), width=2)

        image = image.transpose(Image.FLIP_TOP_BOTTOM)   # Flip the image
        image.show()                                     # Show the result with cell
        image.save('cell_' + result_filename)            # Save the CELL result image


if __name__ == '__main__':
    main()
