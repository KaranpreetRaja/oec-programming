import { ReactPainter } from 'react-painter';

export default function Prompt({ visibility }) {

    const Drawable = () => (
        <ReactPainter
          width={800}
          height={700}
          onSave={blob => console.log(JSON.stringify(blob), blob)}
          render={({ triggerSave, canvas, imageDownloadUrl }) => (
            <div>
              <button onClick={triggerSave}>Save Canvas</button>
              <div className='bg-white'>{canvas}</div>
            </div>
          )}
        />
    );

    return(
        <div className={visibility ? '' : 'hidden'}>
            <Drawable/>
        </div>
    )
}