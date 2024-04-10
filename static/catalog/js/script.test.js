jest.useFakeTimers();

// mock the document.querySelector method
document.querySelector = jest.fn();

// play the header
const header = { style: { filter: '' } };
const featuredProducts = { style: { filter: '' } };

document.querySelector
  .mockReturnValueOnce(header)
  .mockReturnValueOnce(featuredProducts);

// Import the script file
require('./script');

test('header and featuredProducts brightness changes every 2 seconds', () => {
  
  jest.advanceTimersByTime(2000);

  // Check that the brightness of header and featuredProducts has changed
  expect(header.style.filter).toBe('brightness(1.5)');
  expect(featuredProducts.style.filter).toBe('brightness(1.5)');

  
  jest.advanceTimersByTime(2000);


  expect(header.style.filter).toBe('brightness(1)');
  expect(featuredProducts.style.filter).toBe('brightness(1)');
});