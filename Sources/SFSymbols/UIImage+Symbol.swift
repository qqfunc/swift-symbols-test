#if canImport(UIKit)

import UIKit

@available(iOS 2.0, macCatalyst 13.1, visionOS 1.0, watchOS 2.0, *)
public extension UIImage {

    /// Creates an image object that contains a system symbol image.
    /// - Parameter systemSymbol: The system symbol.
    /// - Returns: The object containing the specified symbol image.
    @available(iOS 13.0, macCatalyst 13.1, tvOS 13.0, visionOS 1.0, watchOS 6.0, *)
    convenience init(systemSymbol: SFSymbol) {
        self.init(systemName: systemSymbol.name)!
    }

}

#endif
