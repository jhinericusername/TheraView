import UIKit
import AVKit
import AVFoundation

class RecordingViewController: UIViewController {
    
//    let videoView =
//    @IBOutlet weak var videoContainerView: UIView!

    override func viewDidLoad() {
        super.viewDidLoad()
        

        // Add any setup code you need to run when the view loads
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        let player = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "IMG_1191", ofType: "mp4")!))
        let layer = AVPlayerLayer(player: player)
        layer.frame = view.bounds
        view.layer.addSublayer(layer)
        
        player.play()
    }

 

    // MARK: - IBActions
    // MARK: - Private Methods

}
