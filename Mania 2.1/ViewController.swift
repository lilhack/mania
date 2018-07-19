//
//  ViewController.swift
//  Mania 2.1
//
//  Created by angeliuuu on 2/10/18.
//  Copyright © 2018 Mania Team. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {

    @IBOutlet weak var textName: UITextField!
    @IBOutlet weak var textPhone: UITextField!
    @IBOutlet weak var textEmail: UITextField!
    @IBOutlet weak var textProvider: UITextField!
    @IBOutlet weak var EC1Phone: UITextField!
    // for demo purposes, only the first Emer. Contact's info is saved
    
    func sendRequest() {
        
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        print("hi")
        let base: String = "http://127.0.0.1:5000"
        let route: String = "/api/hello"
        let params: [[String]] = [["name","sylvia"]]
        let url: String = buildURL(base: base, route: route, params: params)
        print(url)
        Mania_2_1.sendRequest(url: "http://127.0.0.1:5000/api/hello?name=sylvia")
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func saveName(_ sender: Any) {
        UserDefaults.standard.set(textName.text, forKey: "savedName")
        UserDefaults.standard.synchronize()
    }
    
    @IBAction func savePhone(_ sender: Any) {
        UserDefaults.standard.set(textPhone.text, forKey: "savedPhone")
       UserDefaults.standard.synchronize()
    }
    
    @IBAction func saveEmail(_ sender: Any) {
         UserDefaults.standard.set(textEmail.text, forKey: "savedEmail")
             UserDefaults.standard.synchronize()
    }
    
    @IBAction func saveProvider(_ sender: Any) {
         UserDefaults.standard.set(textProvider.text, forKey: "savedProvider")
             UserDefaults.standard.synchronize()
    }
    
    @IBAction func saveEC1Phone(_ sender: Any) {
        UserDefaults.standard.set(EC1Phone.text, forKey: "savedEC1Phone")
             UserDefaults.standard.synchronize()
    }

    @IBOutlet weak var myImageView: UIImageView!
    
    @IBAction func openCameraButton(sender: AnyObject) {
        let image = UIImagePickerController()
        image.delegate = self
        image.sourceType = UIImagePickerControllerSourceType.camera
        image.allowsEditing = false
        self.present(image, animated: true)
        {
            
        }
    }
    
    @IBAction func openPhotoLibraryButton(sender: AnyObject) {
            let image = UIImagePickerController()
            image.delegate = self
            image.sourceType = UIImagePickerControllerSourceType.photoLibrary
            image.allowsEditing = false
            self.present(image, animated: true)
            {
                
            }
        }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {
        if let image = info[UIImagePickerControllerOriginalImage] as? UIImage
        {
            myImageView.image = image
        }
        else
        {
            //error message
        }
        self.dismiss(animated: true, completion: nil)
    }
}

func buildURL(base: String, route: String, params: [[String]]) -> String {
    var ret: String
    ret = base + route + "?"
    for param in params {
        ret += param[0] + "=" + param[1] + "&"
    }
    return ret
}

func sendRequest(url: String) {
    let url = URL(string: url)!
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    let postString = ""
    request.httpBody = postString.data(using: .utf8)
    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        guard let data = data, error == nil else {                                                 // check for fundamental networking error
            print("error=\(String(describing: error))")
            return
        }
        
        if let httpStatus = response as? HTTPURLResponse, httpStatus.statusCode != 200 {           // check for http errors
            print("statusCode should be 200, but is \(httpStatus.statusCode)")
            print("response = \(String(describing: response))")
        }
        
        let responseString = String(data: data, encoding: .utf8)
        print("responseString = \(String(describing: responseString))")
    }
    task.resume()
}

