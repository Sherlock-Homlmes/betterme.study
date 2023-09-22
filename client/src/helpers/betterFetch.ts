const fetchWithAuth = async (url: string, options?: any) => {
  const token = window.localStorage.getItem('Authorization');
  return fetch(url, {
    headers: {
      Authorization: token,
    },
    ...options,
  });
};

export default fetchWithAuth;
