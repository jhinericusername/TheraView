import UIKit
import AVKit
import AVFoundation

class PreExerciseViewController: UIViewController {
    
//    let videoView =
//    @IBOutlet weak var videoContainerView: UIView!
//
//    func setUpVideoPlayer() {
//        print("trying to show video")
//        guard let videoURL = Bundle.main.url(forResource: "jj", withExtension: "mp4") else {
//            print("Video not found")
//            return
//        }
//
//        let player = AVPlayer(url: videoURL)
//        let playerLayer = AVPlayerLayer(player: player)
//
//        playerLayer.frame = videoContainerView.bounds
//        playerLayer.videoGravity = .resizeAspect // Adjust this to .resizeAspectFill if you want the video to fill the container view
//        videoContainerView.layer.addSublayer(playerLayer)
//
//        player.play()
//
//        // Loop the video
//        NotificationCenter.default.addObserver(forName: .AVPlayerItemDidPlayToEndTime, object: player.currentItem, queue: .main) { _ in
//            player.seek(to: CMTime.zero)
//            player.play()
//        }
//    }
    override func viewDidLoad() {
        super.viewDidLoad()
        

        // Add any setup code you need to run when the view loads
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        let player = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "jj", ofType: "mp4")!))
        let layer = AVPlayerLayer(player: player)
        layer.frame = view.bounds
        view.layer.addSublayer(layer)
        
        player.play()
    }

 

    // MARK: - IBActions
    // MARK: - Private Methods

}
