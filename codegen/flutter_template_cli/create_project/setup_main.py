from os import path

from codegen.utils.config import Config

def setup_main():
     project_path = Config().get("project_path")
     main_dart_path = path.join(project_path, "lib", "main.dart")
     
     with open(main_dart_path, "w") as file:
        
        file.write(
"""
import 'package:flutter/material.dart';

void main() async{
    WidgetsFlutterBinding.ensureInitialized();
    runApp(MyApp());
}

class MyApp extends StatelessWidget {

    @override
    Widget build(BuildContext context) {
        return MaterialApp(
            title: 'Flutter Demo',
            theme: ThemeData(
                colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
                useMaterial3: true,
            ),
            home: Stack(
                children: [
                    const Text('Template')
                ]
            ),
        );
    }
}
"""
        )
