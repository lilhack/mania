
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        print("hi")
        let base: String = "http://127.0.0.1:5000"
        let route: String = "/api/hello"
        let params: [[String]] = [["name","sylvia"]]
        let url: String = buildURL(base: base, route: route, params: params)
        print(url)
        sendRequest(url: "http://127.0.0.1:5000/api/hello?name=sylvia")
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
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

