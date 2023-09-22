import API_URL from '@/config';
import { useRouter } from 'next/router';
import { useEffect } from 'react';

const Auth = () => {
  const router = useRouter();
  const { query } = useRouter();
  let authApiUrl = API_URL;

  if (
    ['discord-oauth', 'google-oauth', 'facebook-oauth'].includes(
      query.authType as string,
    )
  ) {
    authApiUrl += `/auth/${query.authType}?`;
  }

  useEffect(() => {
    const getAndPersistToken = async () => {
      const res = await fetch(authApiUrl + new URLSearchParams(query as any));
      const data = await res.json();
      if (typeof window !== 'undefined' && data.token) {
        window.localStorage.setItem('Authorization', `Bearer ${data.token}`);
        router.replace(`/dashboard`);
      }
    };

    getAndPersistToken();
  });

  return null;
};
export default Auth;
