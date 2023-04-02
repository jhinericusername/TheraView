import UIKit

class LandingPageViewController: UIViewController {
    
//    let backgroundColor = UIColor(named: "#C9184A")
//    let backgroundColor = UIColor.pink
    let headerLabel = UILabel()
    let descriptionLabel = UILabel()
    let beginCareButton = UIButton()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set the background color
//        self.view.backgroundColor = .systemPink
        
        let outfitSemiHeader = UIFont(name: "Outfit-SemiBold", size: 60)
        let outfitSemiHeader2 = UIFont(name: "Outfit-SemiBold", size: 45)
        let outfitSemiHeader3 = UIFont(name: "Outfit-SemiBold", size: 40)
        let outfitSemiButton = UIFont(name: "Outfit-SemiBold", size: 20)
        let nunitoSubtitle = UIFont(name: "Nunito-Bold", size: 22)
        let nunitoInput = UIFont(name: "Nunito-Bold", size: 14)
        let nunitoBottomScreen = UIFont(name: "Nunito-Regular", size: 18)
        
        let image = UIImage(named: "theraview-low-resolution-logo-white-on-transparent-background")
        

//        // Create the header label
//        headerLabel.text = "Thera View"
//        headerLabel.font = UIFont.systemFont(ofSize: 60, weight: .bold)
//        headerLabel.textColor = .white
//        headerLabel.textAlignment = .center
//
//        // Create the description label
//        descriptionLabel.text = "Your Cooperative Care Companion"
//        descriptionLabel.font = UIFont.systemFont(ofSize: 22, weight: .regular)
//        descriptionLabel.textColor = .white
//        descriptionLabel.textAlignment = .center
        
        // Create the "Begin Care" button
//        beginCareButton.setTitle("BEGIN CARE", for: .normal)
//        beginCareButton.setTitleColor(.black, for: .normal)
//        beginCareButton.backgroundColor = .white
//        beginCareButton.titleLabel?.font = UIFont.systemFont(ofSize: 20, weight: .semibold)
//        beginCareButton.layer.cornerRadius = 8.0
//        beginCareButton.addTarget(self, action: #selector(beginCareButtonTapped), for: .touchUpInside)
        
        // Add the views to the view hierarchy
        view.addSubview(headerLabel)
        view.addSubview(descriptionLabel)
        view.addSubview(beginCareButton)
        
        // Set the constraints for the header label
        headerLabel.translatesAutoresizingMaskIntoConstraints = false
        headerLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20).isActive = true
        headerLabel.bottomAnchor.constraint(equalTo: view.centerYAnchor, constant: -20).isActive = true
        
        // Set the constraints for the description label
        descriptionLabel.translatesAutoresizingMaskIntoConstraints = false
        descriptionLabel.leadingAnchor.constraint(equalTo: headerLabel.leadingAnchor).isActive = true
        descriptionLabel.topAnchor.constraint(equalTo: headerLabel.bottomAnchor, constant: 20).isActive = true
        
        // Set the constraints for the "Begin Care" button
        beginCareButton.translatesAutoresizingMaskIntoConstraints = false
        beginCareButton.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        beginCareButton.bottomAnchor.constraint(equalTo: view.bottomAnchor, constant: -40).isActive = true
        beginCareButton.widthAnchor.constraint(equalToConstant: 200).isActive = true
        beginCareButton.heightAnchor.constraint(equalToConstant: 50).isActive = true
    }
    
    @objc func beginCareButtonTapped() {
        // Handle the "Begin Care" button tap here
    }
}
