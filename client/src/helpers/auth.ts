const isSignedIn = () => {
  const token = window.localStorage.getItem('Authorization');
  return Boolean(token);
};

export default isSignedIn;
