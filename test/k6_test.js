import http from 'k6/http';
import { sleep, check} from 'k6';

export let options = {
    vus: 5,
    duration: '1m'
};

const BASE_URL = 'http://localhost:4000/foo';


export default function () {
    let res = http.get(`${BASE_URL}`);
    check(res, {
<<<<<<< HEAD
        'is response "foobar"': (res) => res.body == 'foobar',
        'is status 200"': (res) => res.status == 200
=======
        'is response "foobar"': (res) => res.body == 'foobar'
>>>>>>> 09b7690ff7226a65c38481e8b735899f9626682d
    });
    sleep(1);
}