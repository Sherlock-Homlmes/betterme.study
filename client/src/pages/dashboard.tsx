import { Layout } from '@/components';
import API_URL from '@/config';
import fetchWithAuth from '@/helpers/betterFetch';
import { useEffect } from 'react';

const Dashboard = () => {
  useEffect(() => {
    const fetchUserInfo = async () => {
      const res = await fetchWithAuth(`${API_URL}/auth/self`);
      const data = await res.json();
      console.log(data);
    };

    fetchUserInfo();
  }, []);

  return (
    <Layout>
      <h2 className='text-3xl font-bold'>Hello, John</h2>
      <h3 className='mt-2 text-gray-400'>Can I tell you a secret?</h3>
      <div className='mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-3'>
        {[...Array(8).keys()].map((n) => (
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
