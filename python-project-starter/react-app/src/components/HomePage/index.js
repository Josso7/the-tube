import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from 'react';
import { getVideos } from '../../store/video';
import './HomePage.css'

function HomePage(){
    const dispatch = useDispatch();

    const videos = useSelector(state => state?.videos?.videos[0]);

    useEffect(() => {
        dispatch(getVideos());
    }, [])

    console.log(videos);

    return (
        <div className='videos-container'>
            {videos && videos.map(video => {
                return (
                <div key={video.id} className='single-video-container'>
                    <video className='video'
                    controls
                    src={video.video_url}
                    ></video>
                    <div className='video-details'>
                        <div className='title'>
                            {video.title}
                        </div>
                        <div className='description'>
                            {video.description}
                        </div>
                    </div>
                </div>
                )
            }
            )}
        </div>
    )
}

export default HomePage;
