
var mongo = require('mongodb');
var http = require('http');

var MongoClient = mongo.MongoClient;
var url = "mongodb+srv://StreetGuardian:jugaadu_coders@streetguardian.j6wtzt6.mongodb.net/?retryWrites=true&w=majority";

const MongoCl = ()=>{
    MongoClient.connect(url, function(err, db) {
        if (err) throw err;
        var dbo = db.db("myDb");
        dbo.createCollection("Users", function(err, res) {
            if (err) throw err;
            console.log("Collection created!");
            db.close();
        });
        console.log("Database created!");
        db.close();

    });
}


http.createServer(function (req, res) {
//   res.writeHead(200, {'Content-Type': 'text/html'});
// MongoCl();
MongoCl();
  res.end('Hello World!');
}).listen(8080);