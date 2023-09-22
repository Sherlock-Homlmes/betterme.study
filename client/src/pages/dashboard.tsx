import { Layout } from '@/components';
import API_URL from '@/config';
import isSignedIn from '@/helpers/auth';
import fetchWithAuth from '@/helpers/betterFetch';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';

interface UserInfo {
  id: string;
  avatar: string;
  name: string;
}

const Dashboard = () => {
  const [user, setUser] = useState<UserInfo>({
    id: '',
    avatar: '',
    name: '',
  });
  const router = useRouter();

  useEffect(() => {
    if (!isSignedIn()) {
      router.push('/sign-in');
      return;
    }

    const fetchUserInfo = async () => {
      try {
        const res = await fetchWithAuth(`${API_URL}/auth/self`);
        const { id, avatar, name } = await res.json();
        setUser({ id, avatar, name });
      } catch (err) {
        // eslint-disable-next-line no-console
        console.error(err);
      }
    };

    fetchUserInfo();
  }, [router]);

  return (
    <Layout>
      <h2 className='text-3xl font-bold'>Xin chào, {user.name}</h2>
      <h3 className='mt-2 text-gray-400'>
        Cùng khám phá hệ sinh thái của BetterMe
      </h3>
      <div className='mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-3'>
        {[...Array(9).keys()].map((n) => (
          <div
            key={n}
            className='h-56 cursor-pointer rounded-md bg-slate-300 transition-colors hover:bg-slate-500 active:bg-slate-900'
          />
        ))}
      </div>
    </Layout>
  );
};

export default Dashboard;
