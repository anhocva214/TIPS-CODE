## How to build mutiple APKs:
1. Change someone line code in file `[ROOT]/android/app/build.gradle`
```
- def enableSeparateBuildPerCPUArchitecture = false
+ def enableSeparateBuildPerCPUArchitecture = true
```
```
- def enableProguardInReleaseBuilds = false
+ def enableProguardInReleaseBuilds = true
```
```
splits {
        abi {
            enable true // <--- add this line
            reset()
            enable enableSeparateBuildPerCPUArchitecture
            universalApk false  // If true, also generate a universal APK
            include "armeabi-v7a", "x86", "arm64-v8a", "x86_64"
        }
    }
```
2. Directional to folder `android` and run `gradle build` on command line

## Someone command line in `android` folder:
```
./gradlew signingReport
```

## Fix Bugs

### 1. Could not find or use auto-linked library 'swiftWebKit'
> Làm theo bước 1 trong bài https://teabreak.e-spres-oh.com/swift-in-react-native-the-ultimate-guide-part-1-modules-9bb8d054db03

### 2. The request was denied by service delegate (SBMainWorkspace)
> I'm new to iOS development. While learning how apple ecosistem is working and trying to set some debugging flags for my iOS app at one point I tried to set an Environment Variable in PRODUCT>SCHEME>EDIT SCHEME, in Arguments tab.
Even though I just hit the plus button to set the new variable without actually setting one I introduced this bug.
After removing the empty environment variable from the scheme everything started working correctly.
Hope this will help others.

### 3. failed to determine clientID - GoogleService-Info.plist was not found and iosClientId was not provided
    Fix: https://stackoverflow.com/questions/45317777/could-not-find-a-valid-googleservice-info-plist-in-your-project

### 4. Tạo icon app cho ios và android:
    https://makeappicon.com/

### 5. Tạo splash screen cho ios:
    Link: https://medium.com/flawless-app-stories/change-splash-screen-in-ios-app-for-dummies-the-better-way-e385327219e

> Thêm `ImageView` thì chọn `View` -> `Show Library`

### 6. Multiple commands produce '/Users/attorneyking/Library/Developer/Xcode/DerivedData/kingattorney-etqotwowxrxhvfavnwycktyoaazs/Build/Products/Debug-iphonesimulator/kingattorney.app/Zocial.ttf': 1) Target 'kingattorney' (project 'kingattorney') has copy command from '/Users/attorneyking/Documents/App/kingattorney/node_modules/react-native-vector-icons/Fonts/Zocial.ttf' to '/Users/attorneyking/Library/Developer/Xcode/DerivedData/kingattorney-etqotwowxrxhvfavnwycktyoaazs/Build/Products/Debug-iphonesimulator/kingattorney.app/Zocial.ttf' 2) That command depends on command in Target 'kingattorney' (project 'kingattorney'): script phase “[CP] Copy Pods Resources”
> https://www.it-swarm-vi.com/vi/info.plist/loi-xcode-10-tao-nhieu-lenh/838444394/

### 8. spawn ./gradlew EACCES
> Run `chmod 755 android/gradlew`


### 9. Exception 'App ID not found. Add a string value with your app ID for the key FacebookAppID to the Info.plist or call [FBSDKSettings setAppID:]

> add `#import <FBSDKCoreKit/FBSDKCoreKit.h>`

> add `[FBSDKApplicationDelegate initializeSDK:launchOptions]; `
