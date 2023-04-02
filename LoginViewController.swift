//import UIKit
//
//class LoginPageViewController: UIViewController {
//
//    // UI Components
//    private let headerLabel = UILabel()
//    private let subHeaderLabel = UILabel()
//    private let emailTextField = UITextField()
//    private let passwordTextField = UITextField()
//    private let loginButton = UIButton()
//    private let signUpPrompt = UILabel()
//    private let backButton = UIButton()
//    private let topRightRectangle = UIView()
//
//    override func viewDidLoad() {
//        super.viewDidLoad()
//
//        setupUI()
//    }
//
//    private func setupUI() {
//        // Header Label
//        headerLabel.text = "Login"
//        headerLabel.font = UIFont.systemFont(ofSize: 45)
//        headerLabel.textColor = .black
//        headerLabel.translatesAutoresizingMaskIntoConstraints = false
//        view.addSubview(headerLabel)
//
//        // Sub-header Label
//        subHeaderLabel.text = "Please sign in to continue."
//        subHeaderLabel.font = UIFont.systemFont(ofSize: 18)
//        subHeaderLabel.textColor = UIColor(red: 126/255, green: 126/255, blue: 126/255, alpha: 1)
//        subHeaderLabel.translatesAutoresizingMaskIntoConstraints = false
//        view.addSubview(subHeaderLabel)
//
//        // Email Text Field
//        emailTextField.backgroundColor = .white
//        emailTextField.layer.cornerRadius = 5
//        emailTextField.placeholder = "EMAIL"
//        emailTextField.addDropShadow(color: UIColor(red: 89/255, green: 13/255, blue: 34/255, alpha: 1))
//        emailTextField.translatesAutoresizingMaskIntoConstraints = false
//        view.addSubview(emailTextField)
//
//        // Password Text Field
//        passwordTextField.backgroundColor = .white
//        passwordTextField.layer.cornerRadius = 5
//        passwordTextField.placeholder = "PASSWORD"
//        passwordTextField.addDropShadow(color: UIColor(red: 89/255, green: 13/255, blue: 34/255, alpha: 1))
//        passwordTextField.translatesAutoresizingMaskIntoConstraints = false
//        view.addSubview(passwordTextField)
//
//        // Login Button
//        loginButton.setTitle("Login", for: .normal)
//        loginButton.titleLabel?.font = UIFont.systemFont(ofSize: 18)
//        loginButton.setBackgroundImage(UIImage(gradientColors: [UIColor(red: 237/255, green: 41/255, blue: 57/255, alpha: 1), UIColor(red: 201/255, green: 24/255, blue: 74/255, alpha: 1)]), for: .normal)
//        loginButton.layer.cornerRadius = 16
//        loginButton.clipsToBounds = true
//        loginButton.translatesAutoresizingMaskIntoConstraints = false
//        view.addSubview(loginButton)
//
//        // Sign Up Prompt
//        signUpPrompt.text = "Don't have an account? Sign Up"
//        signUpPrompt.font = UIFont.systemFont(ofSize: 18)
//        signUpPrompt.translatesAutoresizingMaskIntoConstraints = false
//        view.addSubview(signUpPrompt)
//
//
//        // Back Button (Arrow)
//        backButton.setImage(UIImage(named: "arrow_icon"), for: .normal)
//        backButton.addTarget(self, action: #selector(backButtonTapped), for: .touchUpInside)
//        backButton.translatesAutoresizingMaskIntoConstraints = false
//        view.addSubview(backButton)
//
//        // Top Right Rectangle
//        topRightRectangle.backgroundColor = UIColor(red: 89/255, green: 13/255, blue: 34/255, alpha: 1)
//        topRightRectangle.transform = CGAffineTransform(rotationAngle: CGFloat(-25.15 * Double.pi / 180))
//        topRightRectangle.translatesAutoresizingMaskIntoConstraints = false
//        view.addSubview(topRightRectangle)
//
//        setupConstraints()
//    }
//
//    private func setupConstraints() {
//        // Header Label
//        NSLayoutConstraint.activate([
//            headerLabel.topAnchor.constraint(equalTo: backButton.bottomAnchor, constant: 20),
//            headerLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor)
//        ])
//
//        // Sub-header Label
//        NSLayoutConstraint.activate([
//            subHeaderLabel.topAnchor.constraint(equalTo: headerLabel.bottomAnchor, constant: 10),
//            subHeaderLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor)
//        ])
//
//        // Email Text Field
//        NSLayoutConstraint.activate([
//            emailTextField.topAnchor.constraint(equalTo: subHeaderLabel.bottomAnchor, constant: 40),
//            emailTextField.centerXAnchor.constraint(equalTo: view.centerXAnchor),
//            emailTextField.widthAnchor.constraint(equalToConstant: 355),
//            emailTextField.heightAnchor.constraint(equalToConstant: 49)
//        ])
//
//        // Password Text Field
//        NSLayoutConstraint.activate([
//            passwordTextField.topAnchor.constraint(equalTo: emailTextField.bottomAnchor, constant: 20),
//            passwordTextField.centerXAnchor.constraint(equalTo: view.centerXAnchor),
//            passwordTextField.widthAnchor.constraint(equalToConstant: 355),
//            passwordTextField.heightAnchor.constraint(equalToConstant: 49)
//        ])
//
//        // Login Button
//        NSLayoutConstraint.activate([
//            loginButton.topAnchor.constraint(equalTo: passwordTextField.bottomAnchor, constant: 20),
//            loginButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
//            loginButton.widthAnchor.constraint(equalToConstant: 145),
//            loginButton.heightAnchor.constraint(equalToConstant: 32)
//        ])
//
//        // Sign Up Prompt
//        NSLayoutConstraint.activate([
//            signUpPrompt.bottomAnchor.constraint(equalTo: view.bottomAnchor, constant: -20),
//            signUpPrompt.centerXAnchor.constraint(equalTo: view.centerXAnchor)
//        ])
//
//        // Back Button (Arrow)
//        NSLayoutConstraint.activate([
//            backButton.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 10),
//            backButton.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 10)
//        ])
//
//        // Top Right Rectangle
//        NSLayoutConstraint.activate([
//            topRightRectangle.topAnchor.constraint(equalTo: view.topAnchor, constant: -84),
//            topRightRectangle.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: 170.48),
//            topRightRectangle.widthAnchor.constraint(equalToConstant: 438.21),
//            topRightRectangle.heightAnchor.constraint(equalToConstant: 45.82)
//        ])
//    }
//
//    @objc private func backButtonTapped() {
//        // Implement navigation back to the landing page
//    }
//
//}
//
//
