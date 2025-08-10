#if canImport(SwiftUI)

import SwiftUI

extension Image {

    /// Initializes an `Image` with a system symbol.
    /// - Parameter systemSymbol: The symbol to use for the image.
    public convenience init(systemSymbol: Symbol) {
        self.init(systemName: systemSymbol.rawValue)
            ?? { fatalError("Cannot initialize Image with symbol: \(systemSymbol.rawValue)") }()
    }

}

#endif
