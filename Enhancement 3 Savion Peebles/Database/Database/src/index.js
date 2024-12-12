const polka = require('polka');
const { MongoClient } = require("mongodb");

// Creating a CRUD operation which interacts with a MongoDB NoSQL Database. 
//This project was originally written in Python. It had to converted to JavaScript and MongoDB.

// Creating a document in the Animal Database
polka()
  .get('/create', (req, res) => {
    //Connection to the MongoDB client.
    const client = new MongoClient("mongodb://localhost:27017");
    async function run() {
      try {
        await client.connect();
        const database = client.db("animal");
        const collection = database.collection("names");

        const result = await collection.insertOne({"name":"Sea Urchins"});
        res.end(JSON.stringify(result));
      } catch (e) {
        console.log("Error: " + e);
      } finally {
        await client.close();
      }
    }
    run().catch(console.dir);
  })
  .listen(3000, err => {
    if (err) throw err;
    console.log(`> Running on localhost:3000`);
  });


  // Retrieving a document in MongoDB
  polka()
        .get('/retrieve', (req, res) => {
            const client = new MongoClient("mongodb://localhost:27017");
            async function run() { 
        
              try {
                await client.connect();
                const database = client.db("animals");
                const collection = database.collection("names");
        
                const cursor = collection.find({}, {});
        
                let items = [];
                await cursor.forEach(function(doc){
                  items.push(doc);
                });
                res.end(JSON.stringify(items));
              } catch (error){
                console.warn("ERROR: " + error);
                if (errCallback) errCallback(error);
              } finally {
                await client.close();
              }
            }
            run().catch(console.dir);
          });


// Updating the document in the Database
polka()
        .get('/update', (req, res) => {
            const client = new MongoClient("mongodb://localhost:27017");
            async function run() {
              try {
                await client.connect();
                const database = client.db("animals");
                const collection = database.collection("names");
        
                const updateDoc = {
                  $set: {
                    nickName:
                      "Nickerson",
                  },
                };
        
                const result = await collection.updateOne({}, updateDoc, {}); // <-- empty filter matches all the docs
                res.end("Updated: " + result.modifiedCount);
              } catch (e) {
                errCallback(e);
              } finally {
                // Executes a command to close the connection
                await client.close();
              }
            }
            run().catch(console.dir);
          });

// Deletes a Document in the Animal Database
polka()
    .get('/delete', (req, res) => {
        const client = new MongoClient("mongodb://localhost:27017");
        async function run() {
          try {
            // This is the connection made to the mongoDB database.
            await client.connect();
            const database = client.db("animal");
            const collection = database.collection("names");
            const query = { };
            const result = await collection.deleteOne(query);
            // instruction sent to the database to delete the most recent entry saved
            if (result.deletedCount === 1) {
              res.end("Successfully deleted one document.");
            } else {
              res.end("Deleted 0 documents.");
            }
          } finally {
            await client.close();
          }
        }
    });