const fnWithError = () => {
    throw new Error('Some error');
};

fnWithError();

console.log('Continue...');
