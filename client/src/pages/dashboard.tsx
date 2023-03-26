import { Layout } from '@/components';
import API_URL from '@/config';
import fetchWithAuth from '@/helpers/betterFetch';
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

  useEffect(() => {
    const fetchUserInfo = async () => {
      const res = await fetchWithAuth(`${API_URL}/auth/self`);
      const data = await res.json();
      setUser({
        id: data.id,
        avatar: data.avatar,
        name: data.name,
      } as UserInfo);
    };

    fetchUserInfo();
  }, []);

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
