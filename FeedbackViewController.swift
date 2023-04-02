import UIKit

class FeedbackViewController: UIViewController {

    let circleView = UIView()
    let circleLabel = UILabel()
    

    override func viewDidLoad() {
        super.viewDidLoad()

        
        circleView.backgroundColor = UIColor.systemPink
        circleView.layer.cornerRadius = circleView.bounds.width / 2
        circleView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(circleView)
        
        circleLabel.text = "Hello, World!"
        circleLabel.textColor = UIColor.white
        circleLabel.textAlignment = .center
        circleLabel.translatesAutoresizingMaskIntoConstraints = false
        circleView.addSubview(circleLabel)
        
        // Add positioning constraints
        NSLayoutConstraint.activate([
            circleView.topAnchor.constraint(equalTo: view.topAnchor, constant: 20),
                circleView.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
                circleView.widthAnchor.constraint(equalToConstant: 100),
                circleView.heightAnchor.constraint(equalTo: circleView.widthAnchor),

                circleLabel.centerXAnchor.constraint(equalTo: circleView.centerXAnchor),
            circleLabel.centerYAnchor.constraint(equalTo: circleView.centerYAnchor),
            circleLabel.widthAnchor.constraint(equalTo: circleView.widthAnchor, multiplier: 0.8),
            circleLabel.heightAnchor.constraint(equalTo: circleView.heightAnchor, multiplier: 0.8)
        ])
    }

    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)

        // Add any code you need to run when the view is about to appear
    }

 

    // MARK: - IBActions
    // MARK: - Private Methods

}
