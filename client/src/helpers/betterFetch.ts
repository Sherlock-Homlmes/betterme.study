import Router from 'next/router';

const fetchWithAuth = async (url: string, options?: any) => {
  const token = window.localStorage.getItem('Authorization');
  return !token
    ? Router.push('/sign-in')
    : fetch(url, {
        headers: {
          Authorization: token,
        },
        ...options,
      });
};

export default fetchWithAuth;
