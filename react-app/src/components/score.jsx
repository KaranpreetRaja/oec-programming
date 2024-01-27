import { ReactPainter } from 'react-painter';

export default function Score({ visibility, accuracy}) {

    return(
        <div className={visibility ? '' : 'hidden'}>
            <p className='text-3xl my-24'>Your accuracy is: {accuracy}%</p>
        </div>
    )
}