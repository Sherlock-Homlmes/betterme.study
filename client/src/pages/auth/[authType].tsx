import { useRouter } from 'next/router';
import fetchLink from '@/config';

const Auth = () => {
    // get auth url from router
    const router = useRouter();
    const { query } = useRouter();
    let apiAuthLink = fetchLink

    // 
    if (["discord-oauth", "google-oauth", "facebook-oauth"].includes(query.authType)){
        apiAuthLink += `/auth/${query.authType}?`
    }

    // get JWT token
    fetch(apiAuthLink+ new URLSearchParams(query))
        .then((res) => res.json())
        .then((data) => {
            if (typeof window !== 'undefined' && data.token) {
                window.localStorage.setItem('Authorization', `Bearer ${data.token}`)
                router.replace(`/dashboard`)
            }
        })

    return <p>abc</p>;
}
export default Auth;
