#if canImport(SwiftUI)

import SwiftUI

@available(iOS 13.0, macCatalyst 13.0, macOS 10.15, tvOS 13.0, visionOS 1.0, watchOS 6.0, *)
extension Image {

    /// Initializes an `Image` with a system symbol.
    /// - Parameter systemSymbol: The symbol to use for the image.
    @available(iOS 13.0, macCatalyst 13.0, macOS 11.0, tvOS 13.0, visionOS 1.0, watchOS 6.0, *)
    public init(systemSymbol: SFSymbol) { self.init(systemName: systemSymbol.name) }

}

#endif
