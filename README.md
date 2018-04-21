# tinyappfw
A framework for tiny Android APP development.

## Usage

### Configure maven repository URL
```
repositories {
    google()
    jcenter()
    maven {
        url 'https://raw.githubusercontent.com/tigaliang/tinyappfw/master'
    }
}
```

### Add dependency
```
dependencies {
    implementation 'win.tigaliang:tinyappfw:0.0.1'
}
```

### Source Tree
```
win/
└── tigaliang
    └── tinyappfw
        ├── activities
        │   ├── BaseActivity.java
        │   ├── GridRecyclerViewActivity.java
        │   ├── ListRecyclerViewActivity.java
        │   └── RecyclerViewActivity.java
        └── widgets
            ├── ElegantAdapter.java
            └── HeaderFooterElegantAdapter.java
```

## Sources
https://github.com/tigaliang/ImgurBrowser/tree/master/tinyappfw