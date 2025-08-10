#if canImport(UIKit)

import UIKit

@available(iOS 2.0, macCatalyst 13.1, visionOS 1.0, watchOS 2.0, *)
extension UIImage {

    /// Initializes a `UIImage` with a system symbol.
    /// - Parameter systemSymbol: The symbol to use for the image.
    @available(iOS 13.0, macCatalyst 13.1, tvOS 13.0, visionOS 1.0, watchOS 6.0, *)
    public convenience init(systemSymbol: SFSymbol) {
        self.init(systemName: systemSymbol.rawValue)!
    }

}

#endif
