const userProfile = {
      name: 'Ihor',
      commentQty: 84,
      hasSignedAgreement: false,
};

const userInfo = ({ name, commentQty, hasSignedAgreement }) => {
      if (!commentQty) {
            return `User ${name} has no comments`;
      }
      // const commentsText = hasSignedAgreement ? 'signed' : 'unsigned';
      return `User ${name} has ${commentQty} comments`;
};

const result = userInfo(userProfile);
console.log(result); // Output: User Ihor has unsigned comments
